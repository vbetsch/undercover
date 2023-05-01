from _menu import TestMenu


def call_method(cls, method_name):
    try:
        method = getattr(cls, method_name)
    except AttributeError:
        raise NotImplementedError(
            "Class `{}` does not implement `{}`".format(cls.__class__.__name__, method_name))
    method()


class TestAuto:
    def ta_1(self):
        test_menu = TestMenu()
        # 0->26 TOTAL : (0->16) First letters, (16->32) Numbers, (32->34) Main menu
        for i in range(0, 16):
            print(f"\t- Test #{i + 1}")
            call_method(test_menu, f"test{i + 1}")
            test_menu.menu.run()
        return self


def main():
    print("-> Start tests")
    try:
        for i in range(1):
            call_method(TestAuto(), f"ta_{i + 1}")
    except Exception as e:
        print("###ERROR_FOUND###")
        raise e
    else:
        print("=============== TESTS COMPLETED ===============")
    finally:
        print("-> Finish tests")


if __name__ == '__main__':
    main()
