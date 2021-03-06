from datetime import date
import pytest
from inventory.models import Domain, Subject, Product, UsageType, Usage
from django.contrib.auth.models import User
from accounts.models import Organization
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from django.db.models.deletion import ProtectedError


@pytest.fixture(autouse=True)
def domain():
    return Domain.objects.get(pk=1)


def test_domain_string_representation(domain):
    assert str(domain) == domain.name


def test_domain_name_max_length(domain):
    with pytest.raises(ValidationError):
        domain.name = "x" * 51
        domain.full_clean()


@pytest.fixture
def subject():
    return Subject.objects.get(pk=1)


def test_subject_string_representation(subject):
    assert str(subject) == subject.name


def test_subject_name_max_length(subject):
    with pytest.raises(ValidationError):
        subject.name = "x" * 26
        subject.full_clean()


@pytest.fixture(autouse=True)
def product():
    return Product.objects.get(pk=1)


def test_product_string_representation(product):
    assert str(product) == product.name


def test_product_name_max_length(product):
    with pytest.raises(ValidationError):
        product.name = "x" * 101
        product.full_clean()


def test_product_requires_domain(product, subject):
    with pytest.raises(IntegrityError):
        product = Product.objects.create(name="Test Product 2", subject=subject)
        product.full_clean()


def test_product_subject_can_be_null(product, domain):
    product.subject = None
    product.full_clean()


def test_product_protects_deleting_domain(product, domain):
    with pytest.raises(ProtectedError):
        domain.delete()


def test_product_protects_deleting_subject(product, subject):
    with pytest.raises(ProtectedError):
        subject.delete()


@pytest.fixture
def usage_type():
    return UsageType.objects.get(pk=1)


def test_usage_type_string_representation(usage_type):
    assert str(usage_type) == usage_type.name


def test_usage_type_name_max_length(usage_type):
    with pytest.raises(ValidationError):
        usage_type.name = "x" * 26
        usage_type.full_clean()


@pytest.fixture(autouse=True)
def usage():
    return Usage.objects.get(pk=1)


def test_usage_string_representation(usage):
    assert str(usage) == f"{usage.organization} - {usage.product}"

