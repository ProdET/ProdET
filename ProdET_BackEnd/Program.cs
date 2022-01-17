using Microsoft.EntityFrameworkCore;
using ProdET_BackEnd.Models;

var builder = WebApplication.CreateBuilder(args);

#region Add Services
// Add services to the container.
builder.Services.AddControllers();

builder.Services.AddDbContext<ProductDBContext>(options =>
    //options.UseInMemoryDatabase("ProductList"));  
    options.UseSqlServer(builder.Configuration.GetConnectionString("DevConnection")
     //, b => b.MigrationsAssembly("ProdET_BackEnd.Migrations")
     ));

builder.Services.AddCors();

// Learn more about configuring Swagger/OpenAPI at https://aka.ms/aspnetcore/swashbuckle
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();
#endregion
#region Configuration
var app = builder.Build();

string baseUrl = "https://localhost:3000";
app.UseCors(options =>
options.WithOrigins(baseUrl)
.AllowAnyHeader()
.AllowAnyMethod());

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.UseDeveloperExceptionPage();

    //    app.UseSwagger();
    //    app.UseSwaggerUI();
}

app.UseHttpsRedirection();

app.UseAuthorization();

app.MapControllers();
#endregion

app.Run();
