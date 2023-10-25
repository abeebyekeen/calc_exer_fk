def test_returnSignal(controller):
    """Tests the Return key binding interface to our Qt display widget."""
    from PyQt5 import QtCore, QtGui

    controller._view.setDisplayText("1+2")
    event = QtGui.QKeyEvent(
        QtCore.QEvent.KeyPress, QtCore.Qt.Key_Enter, QtCore.Qt.NoModifier
    )
    controller._view.display.keyPressEvent(event)
    assert controller._view.displayText() == "3"

def test_calculateResult(controller):
    """Tests result."""
    # from PyQt5 import QtCore, QtGui
    controller._view.setDisplayText("4+5")
    # event = QtGui.QKeyEvent(
    #     QtCore.QEvent.KeyPress, QtCore.Qt.Key_Enter, QtCore.Qt.NoModifier
    # )
    # controller._view.display.keyPressEvent(event)
    controller._calculateResult()
    assert controller._view.displayText() == "9"

