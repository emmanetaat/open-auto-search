from dataclasses import dataclass


@dataclass
class Vehicle:
    year: int
    make: str
    model: str
    price: int
    mileage: int


def matches_preferences(
    vehicle: Vehicle,
    max_price: int,
    max_mileage: int,
    min_year: int,
) -> bool:
    """Return True when a vehicle meets the buyer's basic criteria."""
    return (
        vehicle.price <= max_price
        and vehicle.mileage <= max_mileage
        and vehicle.year >= min_year
    )


if __name__ == "__main__":
    example = Vehicle(
        year=2019,
        make="Mercedes-Benz",
        model="C300",
        price=19500,
        mileage=67000,
    )

    print(
        matches_preferences(
            example,
            max_price=22000,
            max_mileage=80000,
            min_year=2016,
        )
    )
