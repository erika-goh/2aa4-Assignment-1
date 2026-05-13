package catandomainmodel;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

class TradeOfferTest {
    @Test
    void testTradeOfferAcceptReject() {
        TradeOffer offer = new TradeOffer(new ResourceHand(), new ResourceHand());
        offer.accept();
        offer.reject();
        assertNotNull(offer);
    }
}
