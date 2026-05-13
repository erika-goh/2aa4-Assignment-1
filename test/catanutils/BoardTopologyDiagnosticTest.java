package catanutils;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertDoesNotThrow;

class BoardTopologyDiagnosticTest {
    @Test
    void testDiagnosticMain() {
        assertDoesNotThrow(() -> BoardTopologyDiagnostic.main(new String[] {}));
    }
}
