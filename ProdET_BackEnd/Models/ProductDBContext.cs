using Microsoft.EntityFrameworkCore;

namespace ProdET_BackEnd.Models
{
    public class ProductDBContext : DbContext
    {
        public ProductDBContext(DbContextOptions<ProductDBContext> options) : base(options)
        {

        }
        public DbSet<Product> Products { get; set; }

    }
}
