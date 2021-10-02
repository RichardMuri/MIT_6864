import torch

__anum = 0


def assert_size(tensor, expected_size):
    if expected_size is torch.Size():
        check_var = expected_size
    else:
        check_var = torch.Size(expected_size)
    ts = tensor.size()
    astring = "Expected tensor of size {}, got: {}".format(check_var, ts)
    assert check_var == ts, astring
    if __name__ == "__main__":
        global __anum
        __anum = __anum + 1
        print("Assertion {} passed".format(__anum))


if __name__ == "__main__":
    tensor = torch.zeros(3, 3, 3)
    expected_size = torch.Size([3, 3, 3])
    assert_size(tensor, expected_size)
    assert_size(tensor, [3, 1, 1])
