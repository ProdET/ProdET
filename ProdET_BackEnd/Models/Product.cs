using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace ProdET_BackEnd.Models
{
    public class Product
    {
        [Key]
        public int Id { get; set; }
        [Column(TypeName = "nvarchar(100)")]
        public string ItemName { get; set; }
        [Column(TypeName = "nvarchar(50)")]
        public string BrandName { get; set; }
        public double Price { get; set; }
        public double Shipping { get; set; }
        [Column(TypeName = "nvarchar(50)")]
        public string Retailer { get; set; }
        [Column(TypeName = "nvarchar(100)")]
        public string Url { get; set; }
    }
}
