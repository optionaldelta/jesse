from jesse.strategies import Strategy


# test_modifying_stop_loss_after_part_of_position_is_already_reduced_with_stop_loss
class Test14(Strategy):
    def should_long(self):
        """

        :return:
        """
        return self.price < 7

    def should_short(self):
        """

        :return:
        """
        return False

    def go_long(self):
        """

        """
        qty = 1.5
        self.buy = qty, 7
        self.stop_loss = [
            (0.5, 6),
            (0.5, 5),
            (0.5, 4)
        ]
        self.take_profit = qty, 13

    def update_position(self):
        """

        """
        if self.is_reduced:
            self.stop_loss = self.position.qty, 4

    def go_short(self):
        """

        """
        pass

    def should_cancel(self):
        """

        :return:
        """
        return False

    def filters(self):
        """

        :return:
        """
        return []
