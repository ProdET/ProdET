namespace ProdET_BackEnd.Models
{
    public class Product
    {
        public int Id { get; set; }
        
        public string? ItemName { get; set; }
        public string? BrandName { get; set; }
        public double Price { get; set; }
        public double Shipping { get; set; }
        public string? Retailer { get; set; }
        public string? Url { get; set; }
        public int? EmissionScore { get; set; }
    }

    /*
     * {"ItemName":"Pixel 6","BrandName":"Google",Price:799.99,"Shipping":0.0,"Retailer":"Amazon","Url":"https://www.amazon.ca/Google-Pixel-Smartphone-Megapixel-Wide-Angle/dp/B09HJZPFDD"}
     * 
     * 
     */
}
