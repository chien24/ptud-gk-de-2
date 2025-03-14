// Hiển thị thông báo
function showNotification(message, type = 'info') {
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type} alert-dismissible fade show`;
    alertDiv.role = 'alert';
    alertDiv.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    `;
    
    const container = document.querySelector('main.container');
    container.insertBefore(alertDiv, container.firstChild);
    
    // Tự động đóng sau 5 giây
    setTimeout(() => {
        const bsAlert = new bootstrap.Alert(alertDiv);
        bsAlert.close();
    }, 5000);
}

// Xác nhận trước khi xóa
function confirmDelete(event, message) {
    if (!confirm(message)) {
        event.preventDefault();
    }
}

// Hiển thị xem trước ảnh khi chọn file
function previewImage(input, imgElement) {
    if (input.files && input.files[0]) {
        const reader = new FileReader();
        
        reader.onload = function(e) {
            imgElement.src = e.target.result;
        }
        
        reader.readAsDataURL(input.files[0]);
    }
}

