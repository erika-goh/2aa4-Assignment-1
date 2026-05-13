package catanutils;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertDoesNotThrow;

class VerifyExportTest {
    @Test
    void testExportMain() {
        assertDoesNotThrow(() -> VerifyExport.main(new String[] {}));
    }
}
