class Check:
    @staticmethod
    def test_temperature_input(temp_str: str) -> bool:
        try:
            int(temp_str)
        except ValueError:
            return False
        return True

    @staticmethod
    def str_to_i(temp_str: str) -> int | None:
        try:
            return int(temp_str)
        except ValueError:
            return None

    @staticmethod
    def is_reasonable(temp: int) -> bool:
        if temp < 0 or temp > 40:
            return False
        return True

    @staticmethod
    def check_temperature(temp_str: str) -> None:
        print(f"Testing temperature: {temp_str}")
        int_temp = Check.str_to_i(temp_str)
        if int_temp is None:
            print(f"Error: '{temp_str}' is not a valid number")
            return
        if Check.is_reasonable(int_temp) is False:
            if int_temp > 40:
                print(f"Error: {int_temp} is too hot for plants(max: 40°C)")
            elif int_temp < 0:
                print(f"Error: {int_temp} is too cold for plants(min: 0°C)")
            return
        print(f"Temperature {int_temp} is perfect for plants!")


if __name__ == "__main__":
    Check.check_temperature(" 25 ")
    print("")
    Check.check_temperature("  abc")
    print("")
    Check.check_temperature("100")
    print("")
    Check.check_temperature("-50")
    print("")

    print("All tests completed - program didn't crash")
