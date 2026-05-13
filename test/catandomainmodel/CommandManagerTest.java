package catandomainmodel;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class CommandManagerTest {

    private CommandManager manager;

    @BeforeEach
    void setUp() {
        manager = new CommandManager();
    }

    @Test
    void testExecuteCommand() {
        GameCommand dummy = new GameCommand() {
            @Override
            public void execute() {
                /* No action needed for test mock */ }

            @Override
            public void undo() {
                /* No action needed for test mock */ }

            @Override
            public String describe() {
                return "Dummy";
            }
        };
        manager.executeCommand(dummy);
        assertTrue(manager.canUndo());
        assertFalse(manager.canRedo());
    }

    @Test
    void testUndoRedo() {
        boolean[] state = { false };
        GameCommand dummy = new GameCommand() {
            @Override
            public void execute() {
                state[0] = true;
            }

            @Override
            public void undo() {
                state[0] = false;
            }

            @Override
            public String describe() {
                return "Dummy";
            }
        };

        manager.executeCommand(dummy);

        assertTrue(manager.undo());
        assertFalse(state[0]);
        assertTrue(manager.canRedo());

        assertTrue(manager.redo());
        assertTrue(state[0]);
    }

    @Test
    void testEmptyUndoRedo() {
        assertFalse(manager.undo());
        assertFalse(manager.redo());
    }
}
